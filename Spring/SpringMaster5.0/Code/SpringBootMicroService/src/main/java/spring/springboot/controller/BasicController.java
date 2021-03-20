package spring.springboot.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class BasicController {

    @GetMapping("/welcome")
    public String welcome(){
        return "Hello World";
    }

    @GetMapping("/welcome-internationalized")
    public String msg(@RequestHeader(value = "Accept-Language", required = false) Locale locale) {
        return messageSource.getMessage("welcome.message", null, locale);
    }
}
