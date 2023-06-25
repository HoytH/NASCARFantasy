FROM node:latest as build
WORKDIR /usr/local/app
COPY ./ /usr/local/app/
RUN npm install
RUN npm run build

FROM nginx:latest
COPY --from=build /usr/local/app/dist/nf-app usr/share/nginx/html
EXPOSE 80
COPY --from=build /usr/local/app/nginx.conf /etc/nginx/conf.d/default.conf