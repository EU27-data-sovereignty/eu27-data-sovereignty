/**
 * The edition for the screens: which one is active, its core part, and the update state (#110, #111), plus
 * the state of the app's own over-the-air update, checked in the same tap (#115). The provider takes the
 * store and the update port, so tests render the real screens on a `MemoryFileStore` edition with no Expo
 * service behind them.
 */
import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useMemo,
  useState,
  type ReactNode,
} from 'react';

import type { CorePart, CountryPart } from '@/data/parts';
import {
  checkForAppUpdate,
  noAppUpdates,
  type AppBuild,
  type AppUpdatePort,
  type AppUpdateState,
} from '@/update/appUpdate';
import { EditionStore, type Edition, type UpdateState } from './EditionStore';

export interface EditionApi {
  store: EditionStore;
  edition: Edition;
  /** Null until the active edition's core part is loaded. */
  core: CorePart | null;
  loadError: string | null;
  update: UpdateState;
  /** The edition check and, in the same tap, the check for a newer build of the app (#115). */
  checkForUpdate(): Promise<void>;
  switchToInstalled(): Promise<void>;
  appUpdate: AppUpdateState;
  build: AppBuild;
  restartToApply(): Promise<void>;
  autoCheck: boolean;
  setAutoCheck(on: boolean): Promise<void>;
  /** The last downloaded part that failed its hash, if the store fell back to the bundled edition. */
  integrityNotice: string | null;
}

const Context = createContext<EditionApi | null>(null);

export function EditionProvider({
  store,
  appUpdates = noAppUpdates,
  children,
}: {
  store: EditionStore;
  appUpdates?: AppUpdatePort;
  children: ReactNode;
}) {
  const [edition, setEdition] = useState<Edition>(store.active);
  const [core, setCore] = useState<CorePart | null>(null);
  const [loadError, setLoadError] = useState<string | null>(null);
  const [update, setUpdate] = useState<UpdateState>({ kind: 'idle' });
  const [appUpdate, setAppUpdate] = useState<AppUpdateState>(
    appUpdates.enabled ? { kind: 'idle' } : { kind: 'disabled' }
  );
  const [autoCheck, setAuto] = useState(false);
  const [integrityNotice, setIntegrityNotice] = useState<string | null>(null);

  const load = useCallback(async () => {
    try {
      const part = await store.core();
      setCore(part);
      setEdition(store.active);
      setIntegrityNotice(store.lastIntegrityError?.message ?? null);
      setLoadError(null);
    } catch (e) {
      setLoadError(e instanceof Error ? e.message : String(e));
    }
  }, [store]);

  // The edition first, then the app's own code: one tap, two hosts, both named on the About screen.
  const checkForUpdate = useCallback(async () => {
    await store.checkForUpdate(setUpdate);
    await checkForAppUpdate(appUpdates, setAppUpdate);
  }, [store, appUpdates]);

  const restartToApply = useCallback(async () => {
    if (appUpdate.kind === 'ready') await appUpdates.reload();
  }, [appUpdates, appUpdate.kind]);

  const switchToInstalled = useCallback(async () => {
    await store.useInstalled();
    setCore(null);
    setUpdate({ kind: 'idle' });
    await load();
  }, [store, load]);

  const setAutoCheck = useCallback(
    async (on: boolean) => {
      await store.setAutoCheck(on);
      setAuto(on);
    },
    [store]
  );

  useEffect(() => {
    let cancelled = false;
    (async () => {
      await store.resolve();
      if (cancelled) return;
      await load();
      const auto = await store.autoCheck();
      if (cancelled) return;
      setAuto(auto);
      if (auto) {
        await store.checkForUpdate((s) => !cancelled && setUpdate(s));
        await checkForAppUpdate(appUpdates, (s) => !cancelled && setAppUpdate(s));
      }
    })();
    return () => {
      cancelled = true;
    };
  }, [store, load, appUpdates]);

  const value = useMemo<EditionApi>(
    () => ({
      store,
      edition,
      core,
      loadError,
      update,
      checkForUpdate,
      switchToInstalled,
      appUpdate,
      build: appUpdates.build,
      restartToApply,
      autoCheck,
      setAutoCheck,
      integrityNotice,
    }),
    [
      store,
      edition,
      core,
      loadError,
      update,
      checkForUpdate,
      switchToInstalled,
      appUpdate,
      appUpdates.build,
      restartToApply,
      autoCheck,
      setAutoCheck,
      integrityNotice,
    ]
  );
  return <Context.Provider value={value}>{children}</Context.Provider>;
}

export function useEdition(): EditionApi {
  const api = useContext(Context);
  if (!api) throw new Error('useEdition() needs an EditionProvider');
  return api;
}

/** One state's part of the active edition; null while loading, with the error if it could not be read. */
export function useCountry(iso: string): { part: CountryPart | null; error: string | null } {
  const { store, edition } = useEdition();
  const key = `${edition.id}/${iso}`;
  const [state, setState] = useState<{
    key: string;
    part: CountryPart | null;
    error: string | null;
  }>({
    key: '',
    part: null,
    error: null,
  });
  useEffect(() => {
    let cancelled = false;
    store
      .country(iso)
      .then((part) => !cancelled && setState({ key, part, error: null }))
      .catch(
        (e: unknown) =>
          !cancelled &&
          setState({ key, part: null, error: e instanceof Error ? e.message : String(e) })
      );
    return () => {
      cancelled = true;
    };
  }, [store, key, iso]);
  // A part loaded for another state or edition is never shown for this one.
  return state.key === key ? { part: state.part, error: state.error } : { part: null, error: null };
}
