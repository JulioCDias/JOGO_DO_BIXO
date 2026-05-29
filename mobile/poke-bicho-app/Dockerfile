FROM node:22-bookworm-slim

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .

EXPOSE 5000

CMD ["sh", "-c", "npm run dev -- --host 0.0.0.0 --port 5000"]
