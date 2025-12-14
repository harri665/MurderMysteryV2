from fastapi import APIRouter

router = APIRouter(
  prefix=''
)

@router.get('/')
def default():
  return {'Hello': 'World'}
