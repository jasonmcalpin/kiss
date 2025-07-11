FROM nginx:alpine

# Copy your HTML, CSS, and JS files
COPY ./public /usr/share/nginx/html
COPY ./src /usr/share/nginx/html/assets

# Expose port 80
EXPOSE 80

# Nginx runs automatically