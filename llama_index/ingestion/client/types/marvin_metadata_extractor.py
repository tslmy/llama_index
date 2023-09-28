# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .metadata_mode import MetadataMode


class MarvinMetadataExtractor(pydantic.BaseModel):
    """
    Base interface for feature extractor.
    """

    is_text_node_only: typing.Optional[bool]
    show_progress: typing.Optional[bool]
    metadata_mode: typing.Optional[MetadataMode]
    marvin_model: typing.Any
    llm_model_string: typing.Optional[str] = pydantic.Field(
        description="The LLM model string to use for extracting custom metadata"
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}