# Plan: a Dutch stichting to house eu27.cloud

Drafted 2026-10-03 by a read-only planning agent and reviewed in session. **This is planning input, not legal
or tax advice.** A notary drafts the statutes, and an accountant or tax adviser checks the ANBI file. External
facts were checked on 2026-10-03 against the sources listed at the end, and anything marked **[unverified]**
could not be confirmed. Founding the entity supersedes DECISIONS #86, so it needs a new decision entry.

## Recommendation

Found a **stichting** with **three board members**, of whom the founder is **not** a majority. Put editorial
independence in the statutes. Apply for **ANBI** within 12 months of founding, so the status applies back to
the founding date. Then move the project's assets over in a fixed order, so nothing breaks.

## Legal form

| Form | Capture-resistance | Fit | Verdict |
|---|---|---|---|
| **Stichting** | High: it has no members, so control can't be bought by joining. The risk of a self-renewing board is handled by clauses | Standard for Dutch NGOs and research projects; eligible for ANBI; grant-makers accept it | **Chosen** |
| Vereniging | Low: an organised membership drive can take over the general meeting (#86) | Good | Rejected |
| Coöperatie | Low: member-controlled, and aimed at members' own interests | Poor | Rejected |
| Foreign or EU form | Varies | No advantage, more administration. The EU cross-border association directive is stalled **[unverified]** | Rejected |

Contributors don't need membership. The reviewer roster and the issue forms already give them a role (#85).

## Statutes: key clauses

Book 2 of the Civil Code (art. 2:286) requires the name, the purpose, how board members are appointed and
dismissed, a seat in the Netherlands, and what happens to any surplus on dissolution. Since the WBTR (1 July
2021), the statutes also need a clause for when all board members are absent or unable to act, and a
conflict-of-interest rule.

1. **Purpose.** "To promote public knowledge of, and democratic oversight over, where and under whose control
   EU member states hold critical government data, through independent research based on public sources,
   published under open licences; not for profit." This fits two ANBI categories: research, and promoting
   the democratic legal order.
2. **Board.**
   - 3 to 7 members, with 4-year terms renewable once.
   - Excluded: anyone employed or paid by a government, an EU body, a cloud provider, or a vendor named in
     the findings.
   - No single person holds a majority.
   - Board members get expenses only. Paid staff are allowed but may not sit on the board.
3. **Conflicts of interest.** A board member with a conflict takes no part in the discussion or the vote. A
   public register of interests is kept.
4. **Editorial independence.** Findings are decided only under a published editorial rulebook, and the board
   cannot overrule an individual finding. Funders, governments and vendors get no say over findings, sources,
   timing or review before publication. Every grant agreement must say so, or the money is refused.
5. **Funding disclosure.** The funder, the amount and the terms are published before the money is accepted.
   Anonymous gifts above a threshold are refused.
6. **Open licences.** Code stays under an OSI licence, and data and text under CC BY 4.0 or more open. A
   licence may never be narrowed.
7. **Entrenchment.** Clauses 1 and 4–6 change only unanimously, with public notice beforehand. Everything
   else needs two-thirds of the board, and every change needs a notarial deed.
8. **Dissolution.** Any surplus goes to an ANBI with a similar purpose. The IP stays open.
9. **The absent-or-unable clause.** If the whole board is absent or unable to act, a named substitute acts and
   appoints a new board.

The two-person rule (#85), the fact-check gate (#87) and the corrections policy belong in the **editorial
rulebook**, not the statutes. That keeps them changeable without a notary, published in git and recorded in
`DECISIONS.md`.

## ANBI

- **Requirements:**
  - at least 90% of activities serve the general interest, with no profit motive;
  - no person controls the assets as if they were their own;
  - reasonable reserves and costs;
  - expense allowances only for board members;
  - a current policy plan;
  - the integrity test: the tax authority may ask for a VOG (certificate of good conduct);
  - a dissolution clause.
- **What to publish on the website:** name, RSIN, contact details, purpose, the main lines of the policy
  plan, the board, the pay policy, and the activity report and accounts within 6 months after year end.
- **Timing:** a decision takes about 8 weeks. The status is backdated to the founding date if the application
  is made within 12 months.
- **SBBI instead:** it gives no tax deduction to donors. ANBI is better here.

## Founding checklist

1. The owner settles the decisions listed at the end.
2. Choose a notary, get a fixed quote, and send a draft of the statutes.
3. Each board member provides ID and signs a conflict-of-interest declaration.
4. Sign the founding deed. The notary registers the stichting with KVK (fee about €85), and it receives an
   RSIN.
5. UBO register: with no one holding over 25% of the votes or actual control, the board members are
   registered as "pseudo-UBOs".
6. Open a business bank account. The bank's checks can take weeks.
7. First board meeting: adopt the editorial rulebook, the policy plan, the pay policy and the funding policy,
   and authorise the transfers.
8. Publish the ANBI page, then apply for ANBI.

## Moving the project in, in this order

1. **Intellectual property.** The founder signs a deed transferring his copyright and database rights to the
   stichting. Copyright transfers only in writing (Auteurswet art. 2). Contributors' CC BY 4.0 and DCO terms
   already cover their work. Add a new copyright line and keep the historical one.
2. **GitHub.** Create an organisation for the stichting, with two owners and 2FA required, and transfer the
   repo.
   - Old URLs redirect, as long as nothing is ever recreated at the old path.
   - Update the hard-coded `github.com/pieteradejong/...` links: `CONTRIBUTING.md`, the generated "Check this
     fact" links, and `LICENSE-DATA`.
3. **Vercel.** Create a team for the stichting; plan for **Pro**, since Hobby is for personal, non-commercial
   use. Transfer the project, which Vercel says happens with no downtime, then:
   - update `VERCEL_ORG_ID` and the `VERCEL_TOKEN` secret;
   - check `VERCEL_PROJECT_ID`;
   - run the `Deploy` workflow and its smoke test.
4. **Domain.** Change the registered owner at iwantmyname. DNS keeps working throughout. A 60-day transfer
   lock after a change of owner may apply **[unverified]**.
5. **Anthropic.** A new organisation and workspace for the stichting, with a spend limit and a new key, set
   through the Vercel dashboard. Then redeploy and revoke the old key.
6. **App stores.** Get a free D-U-N-S number (up to 30 days), then organisation accounts with Apple and
   Google. Apple can waive its fee for a nonprofit that ships only free apps.
7. **Documents.**
   - `docs/editorial-policy.md` ("Who is behind it");
   - a new decision entry that supersedes #86, and #85 reopened;
   - the README, CHANGELOG and `DEPLOYMENT.md`.

## Money

- **Founding:** about €850–1,600 (notary €750–1,500 **[estimate]**, KVK about €85).
- **Each year:** bookkeeping and accounts €600–1,800, bank €100–250 **[estimate]**, directors' liability
  insurance €300–700 **[unverified]**, plus Vercel Pro and the Anthropic spend cap.
- **Funding sources:**

| Source | Size | What to watch |
|---|---|---|
| NLnet | €5k–50k | Open licences required. Its proposal page says it is **not interested in AI-generated projects**, a serious fit risk for an agent-researched project that needs honest framing |
| SIDN fonds | up to €10k; above that, a legal entity is required | The 2026 "digital autonomy" call has closed |
| EMIF, Journalismfund Europe | Competitive | Depends on framing |
| Private foundations, small donations | Varies | Each must pass clause 4 and be published first |

## Privacy

From the transfer on, the stichting is the GDPR controller for anything it collects: a web form, the app, and
`/ask` questions passed on to Anthropic. Before any data collection it needs:
- a privacy notice;
- a record of processing;
- processor agreements with Vercel, Supabase, Anthropic and GitHub;
- transfer safeguards for the US processors.

## Timeline

| Phase | Weeks | Cost |
|---|---|---|
| Decisions, board recruitment, draft statutes | 2–6 | 0 |
| Notary deed, KVK, UBO | 2–4 | €850–1,600 |
| Bank account, policy plan, ANBI page | 2–6 | about €0–250 |
| Transfers | 1–2 | Vercel Pro |
| ANBI application | +8 | 0 |
| D-U-N-S, app accounts, grants, GDPR paperwork | 4–12 | accountant, insurance |

## Risks

- **A self-renewing board drifts.** Mitigated by term limits, the exclusions and the entrenched clauses.
- **The founder stays the de facto controller.** That undermines both ANBI and credibility.
- **Transfers break CI or links.** Follow the order above and run the smoke tests after each step.
- **Grant-makers' stance on AI** (NLnet).
- **Liability for findings about named operators.** Mitigated by insurance and the corrections policy.
- **ANBI duties lapse.**

## Owner decisions

1. The name, checked against KVK and trademarks, and the seat.
2. Three board members, and the founder's own role (board member or editorial lead).
3. Whether to apply for ANBI (recommended).
4. The funding policy: sources, caps, anonymous gifts, and the publication rule.
5. Whether to have paid staff, and whether the founder would be paid.
6. Whether there is a separate editorial board.
7. The notary and the accountant.
8. When to found it, relative to the launch gate (#50).
9. Whether the app is released by the stichting.
10. Whether to join the EU Transparency Register.

## Sources

- KVK, founding a stichting: https://www.kvk.nl/starten/de-stichting/
- KVK, registration fee: https://www.kvk.nl/inschrijven/inschrijfvergoeding/
- KVK, UBOs: https://www.kvk.nl/ubo/wie-zijn-de-ubos-van-je-organisatie-g2/
- KNB, WBTR: https://www.knb.nl/actueel/nieuws/nieuwe-regels-bestuur-toezicht/
- Belastingdienst, ANBI conditions: https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/bijzondere_regelingen/goede_doelen/algemeen_nut_beogende_instellingen/aan_welke_voorwaarden_moet_een_anbi_voldoen/
- Belastingdienst, ANBI publication duties: https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/bijzondere_regelingen/goede_doelen/algemeen_nut_beogende_instellingen/gegevens_van_een_anbi_publiceren_op_een_internetsite/
- Belastingdienst, ANBI with retroactive effect: https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/bijzondere_regelingen/goede_doelen/algemeen_nut_beogende_instellingen/aanwijzing_als_anbi_met_terugwerkende_kracht
- AWR art. 5b: https://wetten.overheid.nl/BWBR0002320
- Auteurswet art. 2: https://wetten.overheid.nl/BWBR0001886
- Civil Code Book 2 **[not fetched]**: https://wetten.overheid.nl/BWBR0003045
- AP, processors: https://autoriteitpersoonsgegevens.nl/nl/onderwerpen/algemene-informatie-avg/verwerkers
- GitHub, transferring a repository: https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository
- Vercel, transferring projects: https://vercel.com/docs/projects/transferring-projects
- Vercel, fair use: https://vercel.com/docs/limits/fair-use-guidelines
- Apple, D-U-N-S: https://developer.apple.com/help/account/membership/D-U-N-S/
- Apple, enrolment and fee waiver: https://developer.apple.com/programs/enroll/
- Google Play, account requirements: https://support.google.com/googleplay/android-developer/answer/13628312
- NLnet, proposals: https://nlnet.nl/propose/
- SIDN fonds: https://www.sidnfonds.nl/aanvragen
- EMIF: https://gulbenkian.pt/emifund/
- Journalismfund Europe: https://www.journalismfund.eu/grants
