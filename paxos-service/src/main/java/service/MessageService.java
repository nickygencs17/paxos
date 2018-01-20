package service;


import com.fasterxml.jackson.databind.JsonNode;
import com.google.common.hash.Hashing;
import org.json.simple.JSONObject;
import org.springframework.web.bind.annotation.*;
import java.nio.charset.StandardCharsets;



@RestController
@RequestMapping("/messages")
public class MessageService{

    public static String DIGEST_CONSTANT = "digest";
    public static String MESSAGE_CONSTANT = "message";




    @RequestMapping(method = RequestMethod.POST)
    public JSONObject createHashService(@RequestBody JsonNode messageJson) {
        String sha256hex = Hashing.sha256()
                .hashString(messageJson.get(MESSAGE_CONSTANT).asText(), StandardCharsets.UTF_8)
                .toString();
        JSONObject jsonObject = new JSONObject();
        jsonObject.put(DIGEST_CONSTANT,sha256hex);
        return jsonObject;
    }



    @RequestMapping(value = "/{hash}", method = RequestMethod.GET)
    public String getMessageService(@PathVariable String hash) {
        return hash;
    }




}
