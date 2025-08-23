package com.decryptr.backend;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import com.decryptr.backend.Decryptor.Decrypt;

@SpringBootApplication
public class BackendApplication {

    public static void main(String[] args) {
        SpringApplication.run(BackendApplication.class, args);

        final int PORT = System.getenv("PORT") != null ? Integer.parseInt(System.getenv("PORT")) : 5173;
        Decrypt decryptor = new Decrypt();
        String key = "";

        System.out.println("Running Decryptr Server on port " + PORT);
    }

}
