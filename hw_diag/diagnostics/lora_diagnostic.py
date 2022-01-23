from hm_pyhelper.diagnostics.diagnostic import Diagnostic

KEY = 'LOR'
FRIENDLY_NAME = "lora"


class LoraDiagnostic(Diagnostic):
    def __init__(self):
        super(LoraDiagnostic, self).__init__(KEY, FRIENDLY_NAME)

    def perform_test(self, diagnostics_report):
        diagnostics_report.record_failure(False, self)
