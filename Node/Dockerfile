# Install build dependancies and build Express app
FROM node:19.7.0-stretch AS build

# Create final image and use PM2 to manage Express app
FROM node:19.7.0-slim AS final
RUN mkdir /app
WORKDIR /app
COPY . .
EXPOSE 4080
CMD ["node", "server.js"]