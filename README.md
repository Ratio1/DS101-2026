# DS101 - Data Science Architects, 2026-2027

DS101 is a graduate course that moves from Data Science fundamentals to neural,
agentic, private, sovereign and operational systems. Fundamentals remain the
spine: every architectural claim must be supported by data, a reproducible
experiment, evaluation evidence and an accountable decision.

## Assessment

- Individual research-paper or approved technical-topic presentation: **30%**.
- End-to-end final project, evidence package, demonstration and oral defense:
  **70%**.

There are no year-specific bonus rules in the 2026 course contract. Students
must be able to explain and defend every submitted artifact, including material
produced with agentic or generative tools.

## Ten-lecture sequence

Each module is one 100-minute lecture. Required preparation and project evidence
do not create undeclared meetings.

1. Data Science Architect roadmap and foundations.
2. Fundamentals I: data, EDA and Pharma.
3. Fundamentals II: modeling, churn and search.
4. NextGenDS I: PyTorch and neural architectures, with a five-minute bounded
   agent-verification bridge.
5. NextGenDS II: accountable agentic workstreams.
6. YourAIYourData I: privacy and confidential processing.
7. Demand forecasting, evaluation and drift.
8. Sovereign, decentralized and edge AI.
9. Productization, distributed MLOps and Ratio1 deployment concepts.
10. Recommenders, Restocracy, governance and defense preparation.

The complete approved plan, timing and delivery boundaries are in
`discipline-syllabus/2026/2026-course-refactor-summary.md`.

## Project contract

Projects use real or credibly acquired data and follow a complete evidence path:

- problem and decision framing;
- provenance, schema, EDA, leakage and split evidence;
- classical and neural baselines with justified evaluation;
- a reproducible model artifact and error analysis;
- an API, container, interface or equivalent operational demonstration;
- agent contracts and traces when agents are used;
- privacy, data-boundary, monitoring, rollback and governance decisions;
- a report, evidence index, repository and oral defense.

The real-estate workflow is the canonical live demonstration. Pharma,
forecasting, stocks/LSTM and Restocracy are transfer or formative cases; the
student-selected end-to-end project is the only 70% graded project.

## Repository map

- `DS101 Lecture 01 ...`: approved 24-slide editable presentation; see the L01 release note below.
- `DS101 Lecture 02 ...` through `DS101 Lecture 10 ...`: reviewed editable releases. All ten root decks are now curated.
- `scripts/lecture_2026_content.py`: superseded L01-L10 specifications retained as historical context, not as the revised deck sources.
- `scripts/build_2026_lecture_decks.py`: verifies and preserves all L01-L10 releases; no active deck is regenerated.
- `scripts/l01_approved_release.py`: checksum and package validation for the approved L01 artifact.
- `scripts/`: inherited notebooks and course utilities.
- `labs/2026/`: bounded agentic, CPU PyTorch, edge-SLM benchmark and offline
  Ratio1 trace assets.
- `real_estate_app/`: FastAPI productization example.
- `mandatory_papers/`: presentation paper pool.
- `discipline-syllabus/2026/`: official fiches and approved refactor plan.
- `discipline-syllabus/docs/`: evidence, inheritance and QA records.
- `_lectures_archives/2025/`: byte-identical archive of the former top-level
  template decks plus selected historical notes and visual evidence.

## Approved L01 revision

The root L01 PowerPoint is the user-approved 24-slide redesign. Its editable
PPTX is the release source; the old Python L01 specification does not reproduce
this design. The build verifies L01 without overwriting it. Missing or changed
L01 files stop the build with an explanation rather than silently restoring the
old deck. Deliberate future edits require renewed review and an updated release
identity in `scripts/l01_approved_release.py`.

See `discipline-syllabus/docs/2026-l01-approved-revision.md` for the slide mapping,
changes, and review limitations. The existing council and 2025 inheritance
records describe the earlier edition. `build_2026_legacy_manifest.py` still
represents that historical generated specification; rerunning it does not
certify the new L01 visuals. The current validator explicitly reports this
limitation while validating all ten curated release identities and their actual notes.

## Rebuild and validate

Run these commands from the repository root with the course Python environment:

```bash
python scripts/curated_lecture_releases.py
python scripts/build_2026_lecture_decks.py
python scripts/validate_2026_lecture_decks.py
```

The official fiches currently declare 28 lecture hours, while the approved ten
100-minute meetings provide 20 academic lecture hours. Faculty approval is
required before changing the signed contact-hour allocation; see the approved
refactor summary for the two reconciliation options.


## Curated L01-L10 presentations

All ten root PowerPoints are reviewed editable release sources: 24, 24, 22, 27,
26, 26, 26, 28, 28 and 28 slides respectively. L04 has 24 teaching slides and
three references; L05 has 24 teaching slides and two references. L06 has 23 main
slides and three references; L07 has 22 main slides and four references.
L08-L10 each have 24 main slides and four references. L06-L10 preserve 35 paper
minutes, 60 instruction/activity minutes and five contingency minutes each.
This L10 publication leaves the other nine presentations unchanged.

The generic builder verifies these files and cannot silently overwrite them.
The L01 guard is unchanged; `scripts/curated_lecture_releases.py` protects L02-L10.
Every entry in `lecture_2026_content.py` is now historical rather than the source
of an active revised design. Deliberate edits require review and a new release
identity; missing or changed releases stop the build while preserving local edits.

Companion source/example bundles are separate conversation deliverables, not
installed by these presentation publications. In particular, the original
`labs/2026/agentic_workstream/fixture.py` remains the old scripted replay. The
new L05 application-level controller and interactive reviewer are in
`DS101_L05_Source_and_Examples.zip`, delivered with the revised presentation.
They must not be confused with the old fixture or a production sandbox.

L02-L04 numerical examples use labeled synthetic data. L05 uses invented
records, scripted proposals, executed application checks and simulated recorded
review. Neither historical-data reproduction nor live-agent productivity is
claimed. Historical visual equivalence remains unverified.

See `discipline-syllabus/docs/2026-l02-l04-approved-revisions.md` and
`discipline-syllabus/docs/2026-l05-approved-revision.md` for exact identities,
validation boundaries, editing guidance and remaining limitations.

## Reviewed L06 privacy presentation

The root L06 deck is the exact reviewed revision, protected against replacement
by the old generator. It connects purpose, exposure, threat, control and
verification through a fictional property request. Local checks concern field
minimization, application logs, authenticated encryption, access revocation and
a designated temporary file. Advanced privacy mechanisms remain conceptual.
These examples do not certify anonymity, production security, secure erasure
or legal compliance. The companion `DS101_L06_Source_and_Examples.zip` remains
a separate delivered package; no original lab is replaced in this commit.
See `discipline-syllabus/docs/2026-l06-approved-revision.md` for the exact file
identity, timing, changes, and publication-validation scope.

## Reviewed L07 forecasting presentation

L07 connects one synthetic daily-delivery decision to the seven-step workflow,
rolling-origin comparison, separate daily/weekly errors, empirical intervals,
drift counterexamples and hypothetical consequences. The nominal 80% band has
71.4% reporting coverage; no coverage guarantee, retailer result, business
savings or live-agent performance is claimed. Its original bytes are protected
from generic regeneration. `DS101_L07_Source_and_Examples.zip` and the review
report remain separate deliverables; existing labs and datasets are unchanged.
See `discipline-syllabus/docs/2026-l07-approved-revision.md` for the file identity,
slide mapping, timing, review results, evidence limits and publication scope.


## Reviewed L08 architecture presentation

The root L08 deck is the exact reviewed 28-slide revision, in the L01-L07 visual
style. Its fictional building-monitoring workload distinguishes data/control
paths, Ratio1 components, node eligibility, application authorization, artifact
identity and answer quality. The companion example executes local integrity,
receiver-failure, queued-delivery and duplicate-safe recovery checks. Two fresh
network-isolated processes exercise only the deterministic fallback.

**The real quantized-SLM benchmark was not run.** Its candidate model and prepared
runner do not supply model-quality, latency, memory, energy or cloud-comparison
results. The slides visibly retain those unmeasured fields. No live Ratio1
network, real sensor, oracle protocol, R1FS/CStore replication or production
resilience is claimed. The original `labs/2026/edge_slm_benchmark/` is unchanged;
`DS101_L08_Source_and_Examples.zip` and the detailed review report remain separate
conversation deliverables, not installed by this presentation-only publication.
See `discipline-syllabus/docs/2026-l08-approved-revision.md` for the exact identity,
slide mapping, timing, review limitations and outstanding execution prerequisite.


## Reviewed L09 productization presentation

L09 is the exact reviewed 28-slide release. The service walkthrough identifies
and migrates the original repository model, versions stricter input rules,
checks numerical parity, distinguishes liveness/readiness from model quality,
and records a local model/configuration rejection-and-restoration sequence.
The 121984.68 reference value is in legacy target units: training provenance,
currency and real-world predictive accuracy are not established.

Docker/container execution and end-to-end browser HTTP were not run. UI checks
used captured-response fixtures; actual loopback HTTP was tested separately.
No live Ratio1, sensor/camera deployment or production security is claimed.
The model/configuration swap used unchanged code, local processes and downtime;
it is not a complete production deployment or database rollback.

`DS101_L09_Source_and_Examples.zip`, the PDF and detailed review remain separate
conversation deliverables. This publication does not replace `real_estate_app/`,
its bundled model, the offline SDK trace or any original lab. See
`discipline-syllabus/docs/2026-l09-approved-revision.md` for identity, timing,
slide mapping, publication validation and outstanding prerequisites.


## Reviewed L10 recommendation and defense presentation

L10 is the exact reviewed 28-slide release, separating text-to-value prediction,
item similarity and user preference. A worked catalog and ranking calculation
connect eligibility, representation comparison, a local withdrawal check and
an evidence-based defense. The 30% individual / 70% final-project assessment
and existing examination arrangements are unchanged.

**The historical Restocracy corpus was not used for the executed benchmark.**
Results use 240 synthetic descriptions and invented targets. The neural model
was selected by development MAE, while ridge has slightly lower reporting-test
MAE; this reversal is retained. Catalog costs, scores and relevance grades are
illustrative, not recovered user behavior. The historical importer was tested
on small fixtures; its integration with the actual corpus remains untested.
No real-user benefit, production readiness or legal compliance is certified.

`DS101_L10_Source_and_Examples.zip`, the PDF and detailed review remain separate
conversation deliverables. This presentation-only publication does not replace
the Restocracy notebooks, data, original labs or previous companion packages.
See `discipline-syllabus/docs/2026-l10-approved-revision.md` for the exact identity,
slide mapping, timing, prior review evidence and publication-validation scope.
