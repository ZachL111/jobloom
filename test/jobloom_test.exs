defmodule JobloomTest do
  use ExUnit.Case

  test "fixture decisions" do
    signal_case_1 = %{demand: 81, capacity: 98, latency: 20, risk: 9, weight: 11}
    assert Jobloom.score(signal_case_1) == 212
    assert Jobloom.classify(signal_case_1) == "accept"
    signal_case_2 = %{demand: 60, capacity: 75, latency: 8, risk: 9, weight: 7}
    assert Jobloom.score(signal_case_2) == 151
    assert Jobloom.classify(signal_case_2) == "review"
    signal_case_3 = %{demand: 86, capacity: 96, latency: 12, risk: 13, weight: 6}
    assert Jobloom.score(signal_case_3) == 183
    assert Jobloom.classify(signal_case_3) == "accept"
  end
end
