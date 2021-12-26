FROM node:17.2.0

WORKDIR /

COPY ./public /public
COPY ./src /src
COPY ./package.json /package.json
COPY ./yarn.lock /yarn.lock

RUN yarn install

CMD [ "yarn", "start" ]

EXPOSE 3000