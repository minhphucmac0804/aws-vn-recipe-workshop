---
title : "Create Qdrant Cloud Collection"
date : 2024-01-01
weight : 1
chapter : false
pre : " <b> 5.3.1. </b> "
---

## Goal

Create the Qdrant Cloud cluster and collection used by the final workshop path.

## Step 1 - Open Qdrant Cloud

1. Sign in to Qdrant Cloud.
2. Create a free-tier or low-cost cluster.
3. Choose a cloud region close enough for workshop testing.
4. Wait until the cluster is ready.

What you should see:

![Qdrant cluster creation](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/01-qdrant-cloud/01-create-cluster.png)

## Step 2 - Open the cluster dashboard

1. Open the cluster dashboard.
2. Confirm the cluster is running.
3. Save the Qdrant URL locally, but do not publish it.

What you should see:

![Qdrant cluster dashboard](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/01-qdrant-cloud/02-cluster-dashboard.png)

## Step 3 - Create the E5 collection

Create the collection:

```text
workshop_vn_recipes_e5_base_cloud
```

Recommended settings:

```text
Vector size: 768
Distance: Cosine
```

Why these settings:

- `768` matches multilingual E5 base embeddings.
- `Cosine` is the intended similarity measure for normalized dense embeddings.

What you should see:

![Qdrant collection creation](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/01-qdrant-cloud/03-collection-creation.png)

## Step 4 - Confirm the empty collection

Before loading data, the collection may be empty. This is expected.

![Empty collection](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/01-qdrant-cloud/05-empty-collection.png)

## What you accomplished

You created the hosted vector collection that the E5 Lambda will query later.
