from pydantic import BaseModel, Field


class Crop(BaseModel):
    crop: str = Field(..., example="Tomato")
    disease: str = Field(..., example="Early Blight")
    confidence: float = Field(..., ge=0, le=100, example=97.5)
    severity: str = Field(..., example="High")


class CropUpdate(BaseModel):
    crop: str | None = None
    disease: str | None = None
    confidence: float | None = Field(default=None, ge=0, le=100)
    severity: str | None = None