package spring.springboot.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;
import spring.springboot.bean.Todo;
import spring.springboot.service.TodoService;

import java.net.URI;
import java.util.List;

@RestController
public class TodoController {

    @Autowired
    private TodoService todoService;

    //리스트 검색
    @ApiOperation(value = "Retrieve all todos for a user by passing in his name", notes = "A list of matching todos is returned. Currently pagination is not supported.", response = Todo.class, responseContainer = "List", produces = "application/json")
    @GetMapping("/users/{name}/todos")
    public List<Todo> retrieveTodos(@PathVariable String name){
        return todoService.retrieveTodos(name);
    }

    //특정 Todo의 세부 정보검색
    @GetMapping(path="/users/{name}/todos/{id}")
    public Todo retrieveTodo(@PathVariable String name, @PathVariable int id){
        Todo todo = todoService.retrieveTodo(id);
        if(todo == null){
            throw new TodonotFoundException("Todo Not Found");
        }

        Resoucre<Todo> todoResource = new Resource<Todo>(todo);
        ControllerLinkBulder linkTo = linkTo(methodOn(this.getClass()).retrieveTodos(name));
        todoResource.add(linkTo.withRel("parent"));

        return todoResource;
    }

    //Todo추가
    @PostMapping("/users/{name}/todos")
    ResponseEntity<?> add(@PathVariable String name, @Valid @RequestBody Todo todo){
        Todo createdTodo = todoService.addTodo(name, todo.getDesc(), todo.getTargetDate(), todo.isDone());
        if(createdTodo == null){
            return ResponseEntity.noContent().build(); //리소스 생성 실패를 반환하는데 사용
        }

        //응답에서 반환된 리소스의 URI를 형식화 한다.
        URI location = ServletUriComponentsBuilder.fromCurrentRequest()
            .path("/{id}").buildAndExpand(createdTodo.getId()).toUri();

        //작성된 리소스에 대한 링크가 있는 상태 201(created)을 반환한다.
        return ResponseEntity.created(location).build();
    }

    @GetMapping(path = "/users/dummy-service")
    public Todo errorService() { throw new RuntimeException("Some Exception Occured"); }
}
