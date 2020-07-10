FROM node:alpine

RUN apk add --update npm 

WORKDIR /aiqdoctests
COPY . .

RUN npm install
RUN npm install nodemon -g

CMD nodemon server.js