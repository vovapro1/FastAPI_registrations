import fastapi_users
import uvicorn

from auth.models import User
from fastapi import Depends, FastAPI
from auth.auth import auth_backend
from auth.manager import get_user_manager
from auth.shemas import UserCreate, UserRead

from operations.router import router as router_operation

app = FastAPI(title="Wood animals")

fastapi_users = fastapi_users.FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

# root на получение пользователя
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

# root на регистрацию
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],)


app.include_router(router_operation)



current_user = fastapi_users.current_user()


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"


@app.get("/unprotected-route")
def unprotected_route():
        return f"Hello, anonym"


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        reload=True,
    )
