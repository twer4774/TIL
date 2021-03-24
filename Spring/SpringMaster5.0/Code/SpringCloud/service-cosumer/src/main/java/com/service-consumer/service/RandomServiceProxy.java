import java.util.List;

import org.springframework.cloud.netflix.feign.FeignClient;
import org.springframework.cloud.netflix.ribbon.RibbonClient;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;


//@FeignClient(name="microservice-a"")
@FeignClient(name="zuul-api-gateway")
@RibbonClient(name="microservice-a")
public interface RandomServiceProxy {
	@RequestMapping(value = "/random", method = RequestMethod.GET)
	public List<Integer> getRandomNumbers();
}