FROM node:16.13.1-alpine
ENV NODE_ENV development

# set work directory
RUN mkdir -p /app
WORKDIR /app

# Install dependencies
COPY ./package.json .
RUN npm install

# Copy app files
COPY . .