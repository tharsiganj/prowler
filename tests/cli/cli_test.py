import json

from typer.testing import CliRunner

from cli.cli import app

runner = CliRunner()


class TestCLI:

    def test_list_services_aws(self):
        result = runner.invoke(app, ["aws", "--list-services"])
        assert result.exit_code == 0
        assert "available services." in result.output

    def test_list_fixers_aws(self):
        result = runner.invoke(app, ["aws", "--list-fixers"])
        assert result.exit_code == 0
        assert "available fixers." in result.output

    def test_list_categories_aws(self):
        result = runner.invoke(app, ["aws", "--list-categories"])
        assert result.exit_code == 0
        assert "available categories." in result.output

    def test_list_compliance_aws(self):
        result = runner.invoke(app, ["aws", "--list-compliance"])
        assert result.exit_code == 0
        assert "available Compliance Frameworks." in result.output

    def test_list_compliance_requirements_aws(self):
        result = runner.invoke(
            app, ["aws", "--list-compliance-requirements", "cis_2.0_aws soc2_aws"]
        )
        assert result.exit_code == 0
        assert "Listing CIS 2.0 AWS Compliance Requirements:" in result.output
        assert "Listing SOC2  AWS Compliance Requirements:" in result.output

    def test_list_compliance_requirements_no_compliance_aws(self):
        result = runner.invoke(app, ["aws", "--list-compliance-requirements"])
        assert result.exit_code == 2
        assert "requires an argument" in result.output

    def test_list_compliance_requirements_one_invalid_aws(self):
        invalid_name = "invalid"
        result = runner.invoke(
            app,
            ["aws", "--list-compliance-requirements", f"cis_2.0_aws {invalid_name}"],
        )
        assert result.exit_code == 0
        assert "Listing CIS 2.0 AWS Compliance Requirements:" in result.output
        assert f"{invalid_name} is not a valid Compliance Framework" in result.output

    def test_list_checks_aws(self):
        result = runner.invoke(app, ["aws", "--list-checks"])
        assert result.exit_code == 0
        assert "available checks." in result.output

    def test_list_checks_json_aws(self):
        result = runner.invoke(app, ["aws", "--list-checks-json"])
        assert result.exit_code == 0
        assert "aws" in result.output
        # validate the json output
        try:
            json.loads(result.output)
        except ValueError:
            assert False

    def test_log_level(self):
        result = runner.invoke(app, ["aws", "--log-level", "ERROR"])
        assert result.exit_code == 0

    def test_log_level_invalid(self):
        result = runner.invoke(app, ["aws", "--log-level", "INVALID"])
        assert result.exit_code == 2
        assert "Log level must be one of" in result.output

    def test_log_level_no_value(self):
        result = runner.invoke(app, ["aws", "--log-level"])
        assert result.exit_code == 2
        assert "Option '--log-level' requires an argument." in result.output

    def test_log_file(self):
        result = runner.invoke(app, ["aws", "--log-file", "test.log"])
        assert result.exit_code == 0

    def test_log_file_no_value(self):
        result = runner.invoke(app, ["aws", "--log-file"])
        assert result.exit_code == 2
        assert "Option '--log-file' requires an argument." in result.output

    def test_only_logs(self):
        result = runner.invoke(app, ["aws", "--only-logs"])
        assert result.exit_code == 0

    def test_status(self):
        result = runner.invoke(app, ["aws", "--status", "PASS"])
        assert result.exit_code == 0

    def test_status_invalid(self):
        result = runner.invoke(app, ["aws", "--status", "INVALID"])
        assert result.exit_code == 2
        assert "Status must be one of" in result.output

    def test_status_no_value(self):
        result = runner.invoke(app, ["aws", "--status"])
        assert result.exit_code == 2
        assert "Option '--status' requires an argument." in result.output

    def test_outputs_formats(self):
        result = runner.invoke(app, ["aws", "--output-filename", "csv html"])
        assert result.exit_code == 0

    def test_outputs_formats_no_value(self):
        result = runner.invoke(app, ["aws", "--output-filename"])
        assert result.exit_code == 2
        assert "Option '--output-filename' requires an argument." in result.output

    def test_output_directory(self):
        result = runner.invoke(app, ["aws", "--output-directory", "test"])
        assert result.exit_code == 0

    def test_output_directory_no_value(self):
        result = runner.invoke(app, ["aws", "--output-directory"])
        assert result.exit_code == 2
        assert "Option '--output-directory' requires an argument." in result.output

    def test_verbose(self):
        result = runner.invoke(app, ["aws", "--verbose"])
        assert result.exit_code == 0

    def test_ignore_exit_code_3(self):
        result = runner.invoke(app, ["aws", "--ignore-exit-code-3"])
        assert result.exit_code == 0

    def test_no_banner(self):
        result = runner.invoke(app, ["aws", "--no-banner"])
        assert result.exit_code == 0

    def test_unix_timestamp(self):
        result = runner.invoke(app, ["aws", "--unix-timestamp"])
        assert result.exit_code == 0

    def test_profile(self):
        result = runner.invoke(app, ["aws", "--profile", "test"])
        assert result.exit_code == 0
