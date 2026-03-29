You are a research extraction agent working inside this repository.

Your task is to re-process only the papers with missing fields in:

`/home/daniel/git/vidiq/reports/title-abstract-conclusion.md`

and update that file in place.

---

### OBJECTIVE

Some entries in `reports/title-abstract-conclusion.md` have `Not found` for their abstract,
conclusion, or both. Re-read the source PDFs for those entries and attempt to fill in the
missing fields using a more permissive extraction strategy (see below).

Do NOT re-process entries that already have both abstract and conclusion.

---

### STEP 1 — IDENTIFY MISSES

Scan `reports/title-abstract-conclusion.md` for every entry where:

- `**Abstract**` is followed by `Not found`, OR
- `**Conclusion**` is followed by `Not found`

Record the filename for each such entry. These are your work list.

---

### STEP 2 — RE-READ EACH PDF

For each filename on the work list, read the corresponding PDF from:

`/home/daniel/git/vidiq/lit-survey/codex/<filename>`

Apply the permissive extraction rules below.

---

### PERMISSIVE EXTRACTION RULES

#### Abstract

If no section is explicitly labelled `Abstract`:

1. Look for the first substantial paragraph that follows the title and author block and
   precedes the introduction. This paragraph often functions as an unlabelled abstract.
2. Accept section labels such as `Summary`, `Overview`, or `Preface` as abstract equivalents.
3. If still not found, write `Not found`.

#### Conclusion

If no section is explicitly labelled `Conclusion` or `Conclusions`:

1. Accept any of the following as conclusion equivalents (case-insensitive):
   - `Discussion`
   - `Discussion and Conclusion`
   - `Concluding Remarks`
   - `Final Remarks`
   - `Summary`
   - `Summary and Conclusion`
   - `Conclusion and Future Work`
   - `Closing Remarks`
   - `Outlook`
2. If none of the above exist, use the final substantive section of the paper only if it
   clearly functions as a wrap-up (i.e. synthesises findings rather than presenting new
   results). Include a note identifying which section was used.
3. If still not found, write `Not found`.

#### Quality bar

- Preserve original wording as closely as possible.
- Remove page-number artifacts, broken headers, and footer noise.
- Do not paraphrase or invent text.
- If extraction is partial or noisy, include the best conservative result and add a
  `**Note**` line describing the issue.

---

### STEP 3 — PROVENANCE LABEL

Whenever you successfully fill in a previously missing field, append this label on its own
line immediately after the extracted text:

- For a filled abstract: `*Abstract added by Claude*`
- For a filled conclusion: `*Conclusion added by Claude*`

Do NOT add the label if the field remains `Not found`.
Do NOT add the label to fields that were already present before this run.

---

### STEP 4 — UPDATE THE REPORT

Edit `reports/title-abstract-conclusion.md` in place:

- Replace `Not found` with the extracted text (plus provenance label) for each field you
  were able to fill.
- Leave all other content exactly as it is.
- Do not reorder entries.
- Do not alter entries that were not on your work list.

---

### STEP 5 — UPDATE THE SUMMARY

Recalculate and update the `## Summary` section at the top of the report to reflect the
new counts:

- Total PDFs processed (unchanged)
- Abstracts found (updated)
- Conclusions found (updated)
- Entries missing either field (updated)

Add a sub-line beneath the existing summary:

`- Re-processing run: <date> — <N> abstracts filled, <N> conclusions filled`

---

### COMPLETION CRITERIA

When finished:

- Every PDF on the work list has been re-examined.
- Every field that could be filled has been filled and labelled.
- Fields that remain missing are still marked `Not found`.
- The `## Summary` counts are accurate.
- Report completion with: total re-examined, abstracts newly filled, conclusions newly
  filled, still missing.
