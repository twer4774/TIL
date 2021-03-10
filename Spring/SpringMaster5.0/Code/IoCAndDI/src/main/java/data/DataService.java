package data;



import beans.Data;
import beans.User;

import java.util.List;

public interface DataService {
    List<Data> retrieveData(User user);
}
