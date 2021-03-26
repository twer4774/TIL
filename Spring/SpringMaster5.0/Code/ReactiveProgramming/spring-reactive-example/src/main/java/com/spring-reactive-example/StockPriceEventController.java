@RestController
public class StockPriceEventController{
    @GetMapping("/stokcs/price/{stockCode}")
    Flux<String> retrieveStockPriceHardcoded(@PathVariable("stockCode") String stockCode){
        return Flux.interval(Duration.ofSeconds(5))
                map(l -> getCurrentDate() + " : "
                + getRandomNumber(100, 125))
                .log();
    }

    private String getCurrentDate(){
        return (new Date()).toString();
    }
    private int getRandomNumber(int min, int max){
        return ThreadLocalRandom.current().nextInt(min, max + 1);
    }
}