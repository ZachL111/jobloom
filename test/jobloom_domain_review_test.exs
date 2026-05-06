defmodule Jobloom.DomainReviewTest do
  use ExUnit.Case

  test "domain review lane" do
    item = %{signal: 55, slack: 44, drag: 30, confidence: 64}
    assert Jobloom.DomainReview.score(item) == 128
    assert Jobloom.DomainReview.lane(item) == "watch"
  end
end
