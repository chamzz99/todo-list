# getting Node 22
FROM node:22-alpine AS builder

# Dir
WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

# NginX
FROM nginx:alpine

#To Nginx Default
COPY --from=builder /app/dist /usr/share/nginx/html

#Port
EXPOSE 80

# Start
CMD ["nginx", "-g", "daemon off;"]