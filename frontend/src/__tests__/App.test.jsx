import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, it, expect, vi } from "vitest";
import App from "../App";

// Mock fetch API
vi.stubGlobal(
  "fetch",
  vi.fn(() =>
    Promise.resolve({
      ok: true,
      json: () =>
        Promise.resolve([
          {
            id: 1,
            title: "Mocked Task",
            description: "Mock description",
            is_completed: false,
          },
        ]),
    }),
  ),
);

describe("To-Do App UI Tests", () => {
  it("renders the main application header", () => {
    render(<App />);
    // Updated to match....
    const headerElement = screen.getByText(/Add a Task/i);
    expect(headerElement).toBeInTheDocument();
  });

  it("renders the add task input and button", () => {
    render(<App />);
    // Updated to match to actual placeholder...
    const inputElement = screen.getByPlaceholderText(/e.g., Buy books/i);
    const buttonElement = screen.getByRole("button", { name: /add/i });

    expect(inputElement).toBeInTheDocument();
    expect(buttonElement).toBeInTheDocument();
  });

  it("allows a user to type in the input field", async () => {
    const user = userEvent.setup();
    render(<App />);

    // Updated to match to actual placeholder..
    const inputElement = screen.getByPlaceholderText(/e.g., Buy books/i);
    await user.type(inputElement, "Study for exam");

    expect(inputElement).toHaveValue("Study for exam");
  });
});
