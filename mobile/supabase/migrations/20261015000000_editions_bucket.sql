-- The edition channel (#111): one public, read-only bucket named `editions`.
--
-- Layout (model/edition.py): <edition>/manifest.json, <edition>/eu27.core.json, <edition>/eu27.<ISO>.json and
-- <edition>/published.json, never overwritten; latest.json, the one mutable pointer. Reads are anonymous: the
-- one `select` policy below is the whole read path, and the anon key the app carries unlocks nothing else.
-- There is deliberately no insert, update or delete policy: only the service role, which bypasses row-level
-- security, writes, and only the deploy workflow holds it (#112). This file is the record of the policy; the
-- hosted project is given the same with `supabase db push`.

insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
values ('editions', 'editions', true, 16777216, array['application/json'])
on conflict (id) do nothing;

create policy "editions are public to read"
on storage.objects for select
to anon, authenticated
using (bucket_id = 'editions');
