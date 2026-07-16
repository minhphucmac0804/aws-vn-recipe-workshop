---
title : "Prepare Qdrant Cloud"
date : 2024-01-01
weight : 3
chapter : false
pre : " <b> 5.3. </b> "
---

## Goal

In this section, you prepare the hosted vector database used by the final Lambda RAG backend.

Qdrant Cloud stores the recipe vectors. Lambda later sends a multilingual E5 query embedding to Qdrant and receives the top-k recipe matches.

## Project progression note

The project did not start directly from the cloud backend. It evolved in stages:

```text
baseline serverless prototype -> local Qdrant retrieval validation -> hosted Qdrant Cloud -> final Lambda RAG backend
```

This context matters because some validation screenshots were produced while the local Qdrant branch was still being used to prove retrieval quality before the hosted backend was complete. The final workshop still focuses on the hosted Qdrant Cloud and Lambda backend path.

## Pages in this section

1. [Create Qdrant Cloud collection](5.3.1-create-gwe/)
2. [Load and verify recipe vectors](5.3.2-test-gwe/)

## Target collection

Use this collection name for the main path:

```text
workshop_vn_recipes_e5_base_cloud
```

Use this broken collection name only for the fallback alarm test later:

```text
workshop_vn_recipes_e5_base_cloud_broken
```

## What you should see by the end

- Qdrant Cloud cluster exists.
- E5 collection exists.
- Collection contains recipe points.
- Direct retrieval or query screenshots show plausible recipe matches.

![Loaded collection](/images/5-Workshop/workshop-005/01-qdrant-cloud/06-loaded-collection.png)
