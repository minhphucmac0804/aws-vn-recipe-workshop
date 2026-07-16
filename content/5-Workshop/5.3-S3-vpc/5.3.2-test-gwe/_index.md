---
title : "Load and Verify Recipe Vectors"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 5.3.2. </b> "
---

## Goal

Load the recipe vectors into Qdrant Cloud and verify that retrieval returns plausible recipe matches.

This page also explains the local Qdrant history. Before the final Lambda RAG backend existed, the project used a local Qdrant branch to validate E5 retrieval. That branch is not the final deployment path, but it explains why retrieval evidence exists before the Lambda backend steps.

## Step 1 - Configure Qdrant settings

In your local `.env`, use the cloud collection:

```text
WORKSHOP_QDRANT_URL=<qdrant-url-redacted>
WORKSHOP_QDRANT_API_KEY=<qdrant-api-key-redacted>
WORKSHOP_QDRANT_COLLECTION=workshop_vn_recipes_e5_base_cloud
```

Do not commit the `.env` file.

## Step 2 - Load vectors

From the project root of the implementation repo, run the loader that builds E5 embeddings and upserts them into Qdrant:

```bash
python3 -m project.extensions.rag.local_qdrant.loader
```

What this command does:

1. reads the recipe dataset
2. creates E5 embeddings
3. connects to Qdrant Cloud
4. inserts recipe vectors and payload metadata

## Step 3 - Check the collection in Qdrant

Open the collection in Qdrant Cloud and confirm that points exist.

What you should see:

![Loaded collection](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/01-qdrant-cloud/06-loaded-collection.png)

Then inspect collection items:

![Collection items](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/01-qdrant-cloud/07-collection-items.png)

## Step 4 - Run a direct retrieval smoke test

Use a known food query such as:

```text
gỏi mít thịt ba chỉ
```

Expected result:

- at least one relevant recipe appears in the result set
- the result is not empty
- retrieved payloads contain recipe names or useful text fields

Evidence examples:

![Qdrant query result 1](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/01-qdrant-cloud/08-result-01.png)
![Qdrant query result 2](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/01-qdrant-cloud/09-result-02.png)
![Qdrant query result 3](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/01-qdrant-cloud/10-result-11.png)

## What you accomplished

You proved that the retrieval layer works before Lambda is introduced. The local Qdrant branch served as the development baseline, and the hosted Qdrant Cloud collection is the collection used by the final Lambda RAG backend.
