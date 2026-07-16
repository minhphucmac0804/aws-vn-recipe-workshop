---
title: "Week 14"
date: 2024-01-01
weight: 14
chapter: false
pre: " <b> 1.14. </b> "
---

**Period:** `08/06/2026 - 14/06/2026`

## Focus

Implemented a Qwen-based version 2 data-processing experiment using Modal GPU resources, then evaluated why the output did not meet the expected quality target.

## Work Completed

- Started running the version 2 data-processing pipeline around 08/06 or 09/06.
- Used a Qwen model through Modal GPU resources while keeping the orchestration code in Colab.
- Produced processed data successfully at the technical execution level.
- Found that the generated data quality was not better than the Gemini-based version 1 output.
- Concluded that stronger infrastructure and a different LLM do not automatically improve dataset quality.

## Daily Progress

| Date | Work completed | Evidence / notes |
| --- | --- | --- |
| 08/06/2026 | Began implementing or preparing the Qwen-based version 2 processing pipeline. | The start came late in the two-week processing period, leaving less time for correction. |
| 09/06/2026 | Ran the Qwen data-processing pipeline using GPU resources through Modal. | The pipeline executed and produced output data. |
| 10/06/2026 | Checked Qwen-generated outputs from the version 2 pipeline. | The pipeline worked technically, but early samples raised concerns about semantic accuracy and usefulness. |
| 11/06/2026 | Compared Qwen-generated attributes against the Gemini-based version 1 output. | The review suggested that the new pipeline did not clearly improve attribute quality. |
| 12/06/2026 | Inspected data-quality failures in the Qwen-based approach. | Identified that model choice and GPU execution did not solve unclear prompts, weak source data, or evaluation gaps. |
| 13/06/2026 | Consolidated findings from the version 2 experiment. | The evaluation showed that the experiment was technically successful but did not meet the dataset-quality goal. |
| 14/06/2026 | Reflected on the outcome and documented the limitation of relying on model choice and GPU execution alone. | Main lesson: task design and source data quality mattered more than model size/infrastructure. |

## Reflection and Lessons Learned

The experiment was technically successful because the code ran and produced data, but it did not meet the broader data-quality goal. Using Modal GPU resources and a Qwen model taught me more about running LLM workloads outside a purely local setup. The main lesson was that model size and infrastructure do not automatically improve output quality when task design, evaluation criteria, and source data quality are weak.
