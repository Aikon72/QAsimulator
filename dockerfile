FROM openjdk:17-jdk-slim

WORKDIR /app

COPY target/*.jar app.jar
COPY src/main/resources/application.properties /app/config/

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "app.jar", "--spring.config.location=/app/config/"]