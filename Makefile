ORGANIZATION="onsightops"
REPOSITORY="pynanny"
TAG="latest"

BASE_IMAGE="python"
IMAGE_TAG="3.8.10"

PLATFORM="linux/arm64"
# PLATFORM="linux/amd64"

# Needed to install packages from private repos
BITBUCKET_USERNAME=""
BITBUCKET_PASSWORD=""

S3_KEY=""
S3_SECRET=""

.PHONY:
	build push run list_platforms

build: 
	docker buildx build \
	--platform ${PLATFORM} \
	--build-arg BITBUCKET_USERNAME=${BITBUCKET_USERNAME} \
	--build-arg BITBUCKET_APP_PASSWORD=${BITBUCKET_PASSWORD} \
	--build-arg BASE_IMAGE=${BASE_IMAGE} \
	--build-arg TAG=${IMAGE_TAG} \
	-t ${ORGANIZATION}/${REPOSITORY}:${TAG} -f docker/Dockerfile .

push: 
	docker push ${ORGANIZATION}/${REPOSITORY}:${TAG}

run:
	docker run -it --rm \
	--network host \
	--name onsight_pynanny \
	-e FSSPEC_S3_KEY=${S3_KEY} \
	-e FSSPEC_S3_SECRET=${S3_SECRET} \
	${ORGANIZATION}/${REPOSITORY}:${TAG}

list_platforms: 
	docker buildx ls