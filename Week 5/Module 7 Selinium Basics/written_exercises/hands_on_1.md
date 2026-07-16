# Hands-On 1 – QA Concepts, Functional Testing & Defect Lifecycle

## Task 1: Map Testing Types to a Real System

### Step 1: Testing Levels

#### Unit Testing
Test the `create_course()` function with valid course data and verify it creates the course object correctly without involving the API or database.

**Classification:** Functional Testing

---

#### Integration Testing
Send a `POST /api/courses/` request and verify the API stores the course in the database and returns HTTP 201 Created.

**Classification:** Functional Testing

---

#### System Testing
Execute the complete workflow:
1. Create a course
2. Retrieve the course
3. Update the course
4. Delete the course

Verify the complete system works correctly.

**Classification:** Functional Testing

---

#### User Acceptance Testing (UAT)
As a college administrator, create a new course and verify that students can enroll in it successfully.

**Classification:** Functional Testing

---

### Non-Functional Test Example

**Performance Testing**

Send 500 concurrent requests to:

`POST /api/courses/`

Verify:
- Response time is acceptable.
- Server remains stable.
- No request failures occur.
- Resource usage remains within acceptable limits.

---

### Step 3: Black-Box Testing vs White-Box Testing

| Black-Box Testing | White-Box Testing |
|-------------------|-------------------|
| Tests functionality without knowing the internal code. | Tests the internal implementation and source code. |
| Focuses on inputs and outputs. | Focuses on code logic, branches, and execution paths. |
| Usually performed by QA Testers. | Usually performed by Developers. |

**QA Tester:** Black-Box Testing

**Developer:** White-Box Testing

---

### Step 4: Formal Test Cases

| Test Case ID | Description | Preconditions | Test Steps | Expected Result | Actual Result | Pass/Fail |
|---------------|-------------|---------------|------------|-----------------|---------------|-----------|
| TC_API_001 | Verify successful course creation using valid input. | API server and database are running. | 1. Send POST request with valid data.<br>2. Observe response. | HTTP 201 Created is returned and course is stored in the database. | | |
| TC_API_002 | Verify validation for missing required fields. | API server is running. | 1. Send POST request with missing mandatory fields.<br>2. Observe response. | Validation error is returned and no course is created. | | |
| TC_API_003 | Verify duplicate course handling. | A course with the same unique identifier already exists (if uniqueness is enforced). | 1. Send POST request with duplicate data.<br>2. Observe response. | Duplicate request is rejected and no duplicate record is created. | | |