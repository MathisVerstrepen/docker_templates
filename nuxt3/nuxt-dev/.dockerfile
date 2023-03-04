FROM alpine:3.17.2

RUN apk add --no-cache yarn

WORKDIR /app

COPY ./package.json /app/package.json

RUN yarn install --prefer-offline --frozen-lockfile && yarn cache clean

COPY . /app

CMD [ "yarn", "dev" ]