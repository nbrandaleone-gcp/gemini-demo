# Suggested Prompts and Notes

# Create a python requirements.txt file for my code

# How do I deploy this python code to Cloud Run
## Suggests a Dockerfile. It looks accurate.

## Suggests docker build and push to gcr.io.  This is now considered an obsolete registry, but a good try.

## Run as a Cloud Service.
gcloud run deploy streamlit-gemini \
--image gcr.io/PROJECT_ID/streamlit-gemini \
--platform managed \
--allow-unauthenticated

# Notice. It does not know what the PROECT_ID is.  We would have to set correct that.

# Easier method to build, store and deploy code to Cloud Run directly
gcloud run deploy --source . streamlit-gemini \
--allow-unauthenticated \
--region us-central1

## Unfortunately, this will not work directly on Argolis, due to Cloud Run security restrictions.
## I am looking into a workaround.

## Attempted on personal account for testing.
## 1) Attempt failed since Vertex AI API was not enabled.  Enabled...
## 2) Second attempt worked.
