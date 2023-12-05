FROM redis:latest

# Expose the Redis port
EXPOSE 3600

# Set the Redis configuration
COPY redis.conf /usr/local/etc/redis/redis.conf
CMD ["redis-server", "/usr/local/etc/redis/redis.conf"]

# docker run -d -p 3600:3600 -v radis_volume:/data --name redis_container redis