# JWT Checker

## Usage

**Just simply type:**

`
python jwt_checker.py <your jwt token here>
`

## Example

**type:**

`
python jwt_checker.py eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ
`

**then it will return:**

```
===================Header===================
{"alg":"HS256","typ":"JWT"}
===================Claims===================
{"sub":"1234567890","name":"John Doe","admin":true}
============================================
```
