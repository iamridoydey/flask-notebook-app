# ===================== Stage 1: Build =====================
FROM node:20-slim AS builder

WORKDIR /app

# Copy dependency manifests
COPY package*.json ./

# Install dependencies
RUN npm ci

# Copy source code
COPY . .

# Build production bundle
RUN npm run build

# ===================== Stage 2: Serve =====================
FROM node:20-slim

WORKDIR /app

# Install a simple static file server
RUN npm install -g serve

# Copy built files from builder
COPY --from=builder /app/dist ./dist

# Expose port 3000
EXPOSE 3000

# Serve static files
CMD ["serve", "-s", "dist", "-l", "3000"]
