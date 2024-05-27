from fastapi import APIRouter, HTTPException, status
from schemas import Product, ProductCreate
from . import crud

router = APIRouter(tags=["Products"])

@router.get(path: "/", response_model=lisy[Product])
async def get_products(session):
    return await crud.get_products(session=session)

@router.post(path: "/", response_model=Product)
async def create_product(session, product_in: ProductCreate):
    return await crud.create_product(session=session, product_in=product_in)


@router.get("/{product_id}/", response_model = Product)
async def get_product(product_id:int, session):
    product = await crud.get_products(session=session, product_id=product_id)
    if product is not None:
        return product

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND
        detail = f"Product {product_id} not found!"

    )
