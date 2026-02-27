from pydantic import BaseModel, Field
class CategoryBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, 
        description="category name")
    slug: str = Field(..., min_length=1, max_length=100,
        description="URL-friendly version of the category name")
    
    class CategoryBaseConfig:
        pass


class CategoryResponse(CategoryBase):
    id: int = Field(..., description="Unique identifier for the category")
    
    class Config:
        from_attributes = True
    
    
