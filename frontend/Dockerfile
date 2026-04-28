FROM node:20-alpine

WORKDIR /app

COPY package.json pnpm-lock.yaml* ./
RUN npm install -g pnpm && pnpm install

COPY . .

EXPOSE 3000
CMD ["pnpm", "dev", "--", "-H", "0.0.0.0", "-p", "3000"]
