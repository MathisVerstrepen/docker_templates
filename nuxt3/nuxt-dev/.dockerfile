FROM alpine:3.17.2

RUN apk add --no-cache \
    bash \
    curl \
    git \
    nodejs \
    npm \
    yarn

WORKDIR /app

COPY ./package.json /app/package.json

RUN yarn install

COPY . /app

CMD [ "yarn", "dev" ]