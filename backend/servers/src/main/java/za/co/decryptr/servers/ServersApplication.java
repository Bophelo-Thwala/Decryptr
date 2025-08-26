package za.co.decryptr.servers;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import io.github.mihkels.dotenv.Dotenv;


@SpringBootApplication
public class ServersApplication {

    public static void main(String[] args) {

        Dotenv dotenv = Dotenv.load();

        final String PORT = dotenv.get("PORT");

        SpringApplication.run(ServersApplication.class, args);

        System.out.println("\nRunning Spring Boot backend at port " + PORT);

        System.out.println("http://localhost:" + PORT);
    }

}
