# AWS Vietnamese Recipe Assistant Workshop

This repository contains my First Cloud Journey internship workshop site for the AWS Vietnamese Recipe Assistant project. The site is built with Hugo using the FCJ workshop template style and is published through GitHub Pages.

## Live Site

View the deployed workshop:

https://minhphucmac0804.github.io/aws-vn-recipe-workshop/

## Overview

The workshop documents a small Vietnamese recipe assistant built around a Lambda-based retrieval augmented generation path. A local Chainlit UI sends recipe questions to an AWS Lambda Function URL. The Lambda backend runs as a container, creates multilingual E5 query embeddings, retrieves relevant recipe context from Qdrant Cloud, asks Gemini to generate a grounded answer, and returns the response to Chainlit.

The workshop also includes reviewer-facing validation and observability evidence using DynamoDB, CloudWatch, EventBridge Scheduler, CloudWatch alarms, and SNS email notification.

## Architecture

Main request path:

```text
Local Chainlit UI
  -> Lambda Function URL
  -> Lambda container with multilingual E5 embeddings
  -> Qdrant Cloud retrieval
  -> Gemini grounded answer
  -> Chainlit response
```

Supporting observability:

```text
Lambda -> DynamoDB query logs
Lambda -> CloudWatch structured logs
EventBridge Scheduler -> Lambda health check
CloudWatch metric filter/alarm -> SNS email notification
```

## Repository Structure

```text
content/        Workshop pages in English and Vietnamese
static/         Images, videos, PDFs, and other static assets
layouts/        Hugo layout overrides and shortcodes
themes/         Hugo Learn theme files
.github/        GitHub Actions deployment workflow
config.toml     Hugo site configuration
```

## Local Preview

Install Hugo, then run:

```bash
hugo server
```

Open the local URL printed by Hugo, usually:

```text
http://localhost:1313/
```

## Deployment

The repository includes a GitHub Actions workflow that builds the Hugo site and publishes the generated output to the `gh-pages` branch for GitHub Pages hosting.

Typical update flow:

```bash
git add .
git commit -m "Update workshop site"
git push
```

After pushing, check the repository Actions tab and wait for the Hugo deployment workflow to complete.

## Bilingual Coverage

The workshop content is provided in English and Vietnamese. The main reviewer-facing sections include the worklog, proposal, blog/event summaries, workshop guide, self-assessment, feedback, and supporting evidence.

## Author

Minh Phuc Mac  
First Cloud Journey internship project  
AWS Vietnamese Recipe Assistant Workshop

## Purpose

This repository is for educational and internship submission purposes. It documents the final workshop path, project background, implementation evidence, evaluation notes, and cleanup evidence for reviewer assessment.
