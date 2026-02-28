import logging
from typing import Any

from langgraph.graph import StateGraph

from src.model.GraphState import GraphState
from src.tool.EngineeringRFCGenerator import generate_rfc
from src.tool.ExportDoc import export_doc
from src.tool.FinaliseRFC import finalise_rfc
from src.tool.SectionParser import parse_section
from src.tool.DocImporter import import_doc

logger = logging.getLogger(__name__)

def _build_graph() -> Any:

    logger.info('building graph')
    workflow = StateGraph(GraphState)

    logger.info('adding nodes')
    workflow.add_node("import_brd", import_doc)
    workflow.add_node("section_parser", parse_section)
    workflow.add_node("rfc_creator", generate_rfc)
    workflow.add_node("finalise_rfc", finalise_rfc)
    workflow.add_node("export_doc", export_doc)

    workflow.set_entry_point("import_brd")
    workflow.add_edge("import_brd", "section_parser")
    workflow.add_edge("section_parser", "rfc_creator")
    workflow.add_edge("rfc_creator", "finalise_rfc")
    workflow.add_edge("finalise_rfc", "export_doc")

    return workflow.compile()

_build_graph = _build_graph()