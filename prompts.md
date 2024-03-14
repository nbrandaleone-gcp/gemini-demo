# Suggested Prompts and Notes

<prompt>
Create a python requirements.txt file for my code
## Two files recommended. I inserted them into requirements.txt

<prompt>
How do I deploy this python code to Cloud Run
## Gemini suggests a Dockerfile. It looks accurate.

## Gemini suggests docker build and push to gcr.io.  This is now considered an obsolete registry, but a good try. Ignore recommendation.

<prompt>
## Gemini suggests the following gcloud command
gcloud run deploy streamlit-gemini \
--image gcr.io/PROJECT_ID/streamlit-gemini \
--platform managed \
--allow-unauthenticated

## Notice. It does not know what the PROECT_ID is.  We would have to correct that.

## There is an easier method to build, store and deploy code to Cloud Run directly
gcloud run deploy --source . streamlit-gemini \
--allow-unauthenticated \
--region us-central1

## Unfortunately, this will not work directly on Argolis, due to Cloud Run security restrictions. We woudld have to override local Org policies.


## Attempted on personal account for testing.
## 1) Attempt failed since Vertex AI API was not enabled.  Enabled...
## 2) Second attempt worked.
