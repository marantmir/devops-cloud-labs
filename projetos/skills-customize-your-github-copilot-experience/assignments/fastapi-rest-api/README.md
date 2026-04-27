# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build robust and scalable REST APIs using FastAPI, a modern Python web framework. You'll understand HTTP methods, request/response handling, and best practices for API design while creating a fully functional API.

## 📝 Tasks

### 🛠️ Create a Basic API with FastAPI

#### Description
Start by setting up a FastAPI application and creating your first endpoints. You'll learn about route decorators, HTTP methods, and basic response handling. This task will help you understand the fundamentals of how requests flow through a web API and how to structure your application.

#### Requirements
Completed program should:

- Import FastAPI and create an application instance
- Create at least 2 GET endpoints that return different responses
- Implement proper HTTP status codes
- Use descriptive docstrings for each endpoint

### 🛠️ Build a Todo List API

#### Description
Create a more complex API that manages a collection of todos. You'll learn about request bodies, data validation, and performing CRUD operations (Create, Read, Update, Delete) on your data.

#### Requirements
Completed program should:

- Create POST endpoint to add new todos
- Create GET endpoint to retrieve all todos or a specific todo by ID
- Create PUT endpoint to update a todo
- Create DELETE endpoint to remove a todo
- Validate incoming data with Pydantic models
- Store todos in a data structure (list or dictionary)

### 🛠️ Add Query Parameters and Path Parameters

#### Description
Enhance your API with flexible query and path parameters. Learn how to extract dynamic data from URLs and query strings to make your API more versatile and powerful.

#### Requirements
Completed program should:

- Use path parameters to identify specific resources
- Implement query parameters for filtering or pagination
- Validate parameter types and values
- Return appropriate error responses for invalid parameters
- Provide clear documentation for all parameters

