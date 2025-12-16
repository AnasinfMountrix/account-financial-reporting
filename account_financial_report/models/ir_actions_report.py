# Copyright 2020 Onestein (<https://www.onestein.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class IrActionsReport(models.Model):
    _inherit = "ir.actions.report"

    @api.model
    def _prepare_account_financial_report_context(self, data):
        lang = data and data.get("account_financial_report_lang") or ""
        return dict(self.env.context or {}, lang=lang) if lang else False

    @api.model
    def _render_qweb_html(self, report_ref, docids, data=None):
        context = self._prepare_account_financial_report_context(data)
        obj = self.with_context(**context) if context else self
        return super(IrActionsReport, obj)._render_qweb_html(
            report_ref, docids, data=data
        )

    @api.model
    def _render_xlsx(self, report_ref, docids, data=None):
        # #region agent log
        try:
            import json as _json
            import os as _os
            _log_path = '/Users/agustin/Dev/Mountrix/nabrawind/.cursor/debug.log'
            _os.makedirs(_os.path.dirname(_log_path), exist_ok=True)
            with open(_log_path, 'a') as _f:
                _f.write(_json.dumps({"id":"log_render_xlsx_entry","timestamp":__import__('time').time()*1000,"location":"ir_actions_report.py:24","message":"_render_xlsx entry","data":{"data_keys":list(data.keys()) if data else None,"has_wizard_name":data.get("wizard_name") if data else None,"has_wizard_id":data.get("wizard_id") if data else None,"data_is_none":data is None},"sessionId":"debug-session","runId":"run1","hypothesisId":"H2"})+"\n")
        except Exception:
            pass
        # #endregion
        context = self._prepare_account_financial_report_context(data)
        obj = self.with_context(**context) if context else self
        return super(IrActionsReport, obj)._render_xlsx(report_ref, docids, data=data)
