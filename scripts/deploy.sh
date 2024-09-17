#!/bin/bash

set -e

# Authenticate with Google Cloud
echo "Authenticating with Google Cloud..."
gcloud auth activate-service-account --key-file=$GCP_SERVICE_ACCOUNT_KEY

# Build and push Docker images
echo "Building and pushing Docker images..."
docker build -t gcr.io/$GCP_PROJECT_ID/backend:$VERSION ./backend
docker build -t gcr.io/$GCP_PROJECT_ID/frontend:$VERSION ./frontend
docker push gcr.io/$GCP_PROJECT_ID/backend:$VERSION
docker push gcr.io/$GCP_PROJECT_ID/frontend:$VERSION

# Update Google Cloud Run services
echo "Updating Google Cloud Run services..."
gcloud run deploy backend --image gcr.io/$GCP_PROJECT_ID/backend:$VERSION --platform managed --region $GCP_REGION
gcloud run deploy frontend --image gcr.io/$GCP_PROJECT_ID/frontend:$VERSION --platform managed --region $GCP_REGION

# Apply database migrations
echo "Applying database migrations..."
gcloud run jobs execute apply-migrations --region $GCP_REGION

# Update environment variables
echo "Updating environment variables..."
gcloud run services update backend --set-env-vars="DB_URL=$DB_URL,API_KEY=$API_KEY" --region $GCP_REGION
gcloud run services update frontend --set-env-vars="BACKEND_URL=$BACKEND_URL" --region $GCP_REGION

# Perform smoke tests
echo "Performing smoke tests..."
# HUMAN ASSISTANCE NEEDED
# Add specific smoke test commands here. For example:
# curl -f https://backend-url/health
# curl -f https://frontend-url

# Notify team of deployment status
echo "Notifying team of deployment status..."
# HUMAN ASSISTANCE NEEDED
# Add notification mechanism here. For example:
# slack-notify "Deployment of version $VERSION completed successfully"

echo "Deployment completed successfully!"