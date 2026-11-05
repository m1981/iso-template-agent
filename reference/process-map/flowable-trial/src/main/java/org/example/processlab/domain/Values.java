package org.example.processlab.domain;

import java.util.Objects;

final class Values {
    private Values() {}

    static String nonBlank(String value, String name) {
        Objects.requireNonNull(value, name);
        if (value.isBlank()) {
            throw new IllegalArgumentException(name + " must not be blank");
        }
        return value;
    }
}
