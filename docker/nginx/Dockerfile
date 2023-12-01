FROM node:18.16-alpine AS build

WORKDIR /app/front

COPY ./front ./

FROM nginx:1.23.2-alpine

COPY --from=build /app/front /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]
