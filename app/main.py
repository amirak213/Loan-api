from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.loan import monthly_payment

app = FastAPI(title="Loan API")


class LoanRequest(BaseModel):
    principal: float = Field(gt=0)
    annual_rate: float = Field(ge=0)
    months: int


class LoanResponse(BaseModel):
    payment: float


@app.post("/monthly-payment", response_model=LoanResponse)
def compute_monthly_payment(request: LoanRequest):

    try:
        resultat = monthly_payment(
            request.principal, request.annual_rate, request.months
        )
    except ValueError as erreur:
        raise HTTPException(status_code=400, detail=str(erreur))
    return LoanResponse(payment=resultat)
